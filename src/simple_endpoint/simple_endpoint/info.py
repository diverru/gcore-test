import pygit2

from datetime import datetime
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


# remember time of the first import=time of the application start
STARTED_TS = datetime.utcnow()


@api_view()
def get_info(request):
    now = datetime.utcnow()
    repo = pygit2.Repository(settings.REPO_PATH)
    head = repo.head
    last_commit = head.peel()
    commit_timestamp = last_commit.commit_time
    commit_dt = datetime.fromtimestamp(commit_timestamp)
    # not sure whether there is a better way
    version_info = repo.describe(max_candidates_tags=1, describe_strategy=pygit2.GIT_DESCRIBE_TAGS)
    result = {
        "commit": last_commit.hex,
        "commit_date": commit_dt.isoformat() + 'Z',
        "version": version_info,
        "branch": head.shorthand,
        "uptime": int((now - STARTED_TS).total_seconds()),
        "started": STARTED_TS.replace(microsecond=0).isoformat() + "Z"
    }
    return Response(result)
