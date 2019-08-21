# base python image
FROM python:3.5.7

# set working directory
WORKDIR '/app'

RUN pip3 install --upgrade pip && \
    pip3 install Django gunicorn graphene_django psycopg2-binary


# move backend directory into root of app directory
# OK b/c backend image contains no frontend code
COPY ./ ./
RUN mv ./synth_project/settings_prod.py ./synth_project/settings.py

EXPOSE 5005
CMD ["gunicorn", "--bind", "0.0.0.0:5005", "--workers", "4", "synth_project.wsgi"]
