# Lint as: python3
import datasets
import os
from pathlib import Path
from datasets import ClassLabel, DownloadConfig
"""The JPN Dataset."""

import datasets

logger = datasets.logging.get_logger(__name__)

_CITATION = """"""

_DESCRIPTION = """"""

_URL = "https://raw.githubusercontent.com/ctava/job-position-names-datasets/main/2024-01/"
_TRAINING_FILE = "position_names_train.txt"
_DEV_FILE = "position_names_validate.txt"
_TEST_FILE = "position_names_test.txt"


class JPNConfig(datasets.BuilderConfig):
    """The JPN  Dataset."""

    def __init__(self, **kwargs):
        """BuilderConfig for JPN.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(JPNConfig, self).__init__(**kwargs)


class JPN(datasets.GeneratorBasedBuilder):
    """The JPN  Dataset."""

    BUILDER_CONFIGS = [
        JPNConfig(
            name="jpn", version=datasets.Version("1.0.0"), description="The JPN Dataset"
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-POS",
                                "I-POS"
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
            homepage="",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {
            "train": f"{_URL}{_TRAINING_FILE}",
            "dev": f"{_URL}{_DEV_FILE}",
            "test": f"{_URL}{_TEST_FILE}",
        }
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["validate"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            current_tokens = []
            current_labels = []
            sentence_counter = 0
            for row in f:
                row = row.rstrip()
                if row:
                    token, label = row.split(" ")
                    current_tokens.append(token)
                    current_labels.append(label)
                else:
                    # New sentence
                    if not current_tokens:
                        # Consecutive empty lines will cause empty sentences
                        continue
                    assert len(current_tokens) == len(current_labels), "💔 between len of tokens & labels"
                    sentence = (
                        sentence_counter,
                        {
                            "id": str(sentence_counter),
                            "tokens": current_tokens,
                            "ner_tags": current_labels,
                        },
                    )
                    sentence_counter += 1
                    current_tokens = []
                    current_labels = []
                    yield sentence
            # Don't forget last sentence in dataset 🧐
            if current_tokens:
                yield sentence_counter, {
                    "id": str(sentence_counter),
                    "tokens": current_tokens,
                    "ner_tags": current_labels,
                }

class JPNDataset(object):
    """
    """
    NAME = "JPNDataset"

    def __init__(self):
        cache_dir = os.path.join(str(Path.home()), '.cache')
        print("Cache directory: ", cache_dir)
        os.makedirs(cache_dir, exist_ok=True)
        download_config = DownloadConfig(cache_dir=cache_dir)
        self._dataset = JPN(cache_dir=cache_dir)
        print("Cache1 directory: ",  self._dataset.cache_dir)
        self._dataset.download_and_prepare(download_config=download_config)
        self._dataset = self._dataset.as_dataset()

    @property
    def dataset(self):
        return self._dataset

    @property
    def labels(self) -> ClassLabel:
        return self._dataset['train'].features['ner_tags'].feature.names

    @property
    def id2label(self):
        return dict(list(enumerate(self.labels)))

    @property
    def label2id(self):
        return {v: k for k, v in self.id2label.items()}

    def train(self):
        return self._dataset['train']

    def test(self):
        return self._dataset["test"]

    def validation(self):
        return self._dataset["validation"]


if __name__ == '__main__':
    dataset = JPNDataset().dataset

    print(dataset['train'])
    print(dataset['test'])
    print(dataset['validation'])

    print("List of tags: ", dataset['train'].features['ner_tags'].feature.names)


    print("First sample: ", dataset['train'][0])