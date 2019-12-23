import logging
import os

from flask import Blueprint, redirect, request
from injector import inject

from ...helpers import FileHelper
from ...services import JobService
from .responses import Error, Job, Jobs

app = Blueprint('api', __name__)


@app.route('/jobs', methods=["GET"])
@inject
def index(job_service: JobService):
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)
    jobs = job_service.get_jobs(offset, limit)

    return Jobs(jobs).response(), 200


@app.route('/jobs', methods=["POST"])
@inject
def create(job_service: JobService):
    files = []
    temporary_paths = []

    if 'file[]' in request.files:
        for file_ in request.files.getlist("file[]"):
            temporary_path = FileHelper.get_temporary_file()
            temporary_paths.append(temporary_path)
            file_.save(str(temporary_path.resolve()))

            data = {
                'media_type': file_.content_type,
                'name': file_.filename,
                'path': temporary_path,
            }
            files.append(data)

    job = job_service.create_job({
        "data": request.form.get('data'),
        "files": files
    })

    [os.remove(str(path.resolve())) for path in temporary_paths]

    return Job(job).response(), 201


@app.route('/jobs/<string:job_id>', methods=["GET"])
@inject
def get(job_id: str, job_service: JobService):
    job = job_service.get_job(job_id)
    if job is None:
        return Error("Job Not Found").response(), 404

    return Job(job).response(), 200


@app.route('/files/<string:job_file_id>', methods=["GET"])
@inject
def file(job_file_id: str, job_service: JobService):
    url = job_service.get_file_url(job_file_id)
    if url is None:
        return Error("File Not Found").response(), 404

    return redirect(url)
