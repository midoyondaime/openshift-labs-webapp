# openshift-labs-webapp

Tiny Python app used in my OpenShift lab series.

- `GET /` -> `{"app": "webapp", "version": "$APP_VERSION"}`
- `GET /healthz` -> 200
- Port 8080, standard library only.
