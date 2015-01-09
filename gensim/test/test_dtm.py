#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Automated tests for DTM/DIM model
"""


import logging
import gensim
import os
import unittest
from gensim import corpora


# needed because sample data files are located in the same folder
module_path = os.path.dirname(__file__)
datapath = lambda fname: os.path.join(module_path, 'test_data', fname)


class TestDtmModel(unittest.TestCase):

    def setUp(self):
        self.time_slices = [3, 7]
        self.corpus = corpora.mmcorpus.MmCorpus(datapath('dtm_test.mm'))
        self.id2word = corpora.Dictionary.load(datapath('dtm_test.dict'))
        # first you need to setup the environment variable $DTM_PATH for the dtm executable file
        self.dtm_path = os.environ.get('DTM_PATH', None)
        if self.dtm_path is None:
            self.skipTest("$DTM_PATH is not properly set up.")

    def testDtm(self):
        model = gensim.models.DtmModel(self.dtm_path, self.corpus, self.time_slices, num_topics=2, id2word=self.id2word, model='dtm', initialize_lda=True)
        topics = model.show_topics(topics=2, times=2, topn=10)

    def testDim(self):
        model = gensim.models.DtmModel(self.dtm_path, self.corpus, self.time_slices, num_topics=2, id2word=self.id2word, model='fixed', initialize_lda=True)
        topics = model.show_topics(topics=2, times=2, topn=10)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
