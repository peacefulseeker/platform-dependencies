import os
from statistics import mean, pstdev, stdev, pvariance, variance
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'testfiles_number_loc.txt'
STATS = os.path.join(TMP, DATA)
if not os.path.isfile(STATS):
    urlretrieve(os.path.join(S3, DATA), STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""

def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    with open(STATS) as f:
        return [int(line.strip().split(' ')[0]) for line in f]



def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())
    # taking a sample for the last section
    sample = list(data)[::2]
    # # TODO 2: complete this dict, use data list and
    # # for the last 3 sample_ variables, use sample list
    stats = dict(
        count=len(data),
        min_=min(data),
        max_=max(data),
        mean=mean(data),
        pstdev=pstdev(data),
        pvariance=pvariance(data),
        sample_count=len(sample),
        sample_stdev=stdev(sample),
        sample_variance=variance(sample),
    )

    return STATS_OUTPUT.format(**stats)

print(create_stats_report())
