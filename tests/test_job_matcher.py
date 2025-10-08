
from src.nlp.job_matcher import JobMatcher
import os, tempfile



def test_job_matcher_basic(tmp_path):
    # create a fake job file
    jpath = tmp_path / "data_scientist.txt"
    jpath.write_text("Looking for Python and SQL skills, experience with Pandas and Scikit-learn.")
    jm = JobMatcher(str(tmp_path))
    res = jm.match("I have experience in Python, SQL and Pandas.", top_k=1)
    assert isinstance(res, list)

