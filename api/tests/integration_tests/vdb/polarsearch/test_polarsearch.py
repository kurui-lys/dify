import environs

from core.rag.datasource.vdb.polarsearch.polarsearch_vector import PolarSearchVectorStore, PolarSearchVectorStoreConfig
from tests.integration_tests.vdb.test_vector_store import AbstractVectorTest, setup_mock_redis

env = environs.Env()


class Config:
    SEARCH_ENDPOINT = env.str("SEARCH_ENDPOINT", "http://pc-*******************.polardbsearch.rds.aliyuncs.com:3001")
    SEARCH_USERNAME = env.str("SEARCH_USERNAME", "ADMIN")
    SEARCH_PWD = env.str("SEARCH_PWD", "ADMIN")
    USING_UGC = env.bool("USING_UGC", True)


class TestPolarSearchVectorStore(AbstractVectorTest):
    def __init__(self):
        super().__init__()
        self.vector = PolarSearchVectorStore(
            collection_name=self.collection_name,
            config=PolarSearchVectorStoreConfig(
                hosts=Config.SEARCH_ENDPOINT,
                username=Config.SEARCH_USERNAME,
                password=Config.SEARCH_PWD,
            ),
        )

    def get_ids_by_metadata_field(self):
        ids = self.vector.get_ids_by_metadata_field(key="doc_id", value=self.example_doc_id)
        assert ids is not None
        assert len(ids) == 1
        assert ids[0] == self.example_doc_id


class TestPolarSearchVectorStoreUGC(AbstractVectorTest):
    def __init__(self):
        super().__init__()
        self.vector = PolarSearchVectorStore(
            collection_name="ugc_index_test",
            config=PolarSearchVectorStoreConfig(
                hosts=Config.SEARCH_ENDPOINT,
                username=Config.SEARCH_USERNAME,
                password=Config.SEARCH_PWD,
                using_ugc=Config.USING_UGC,
            ),
            routing_value=self.collection_name,
        )

    def get_ids_by_metadata_field(self):
        ids = self.vector.get_ids_by_metadata_field(key="doc_id", value=self.example_doc_id)
        assert ids is not None
        assert len(ids) == 1
        assert ids[0] == self.example_doc_id


def test_polarsearch_vector_ugc(setup_mock_redis):
    TestPolarSearchVectorStore().run_all_tests()
    TestPolarSearchVectorStoreUGC().run_all_tests()