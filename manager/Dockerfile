FROM --platform=linux/x86_64 ghcr.io/everest/build-kit-alpine:v1.1.2

ARG EVEREST_VERSION=charin-e2e-demo
ENV EVEREST_VERSION=charin-e2e-demo

COPY install.sh ./

# Cloning the repo now and copying files over
RUN git clone https://github.com/US-JOET/everest-core.git \
        && cd everest-core \
        && git checkout ${EVEREST_VERSION} \
        && cd .. \
        && mkdir -p /ext/scripts \
        && mv install.sh /ext/scripts/install.sh \
        && mv everest-core /ext/source \
        # Don't run the test-and-install script since it deletes the build directory!
        && /entrypoint.sh run-script install

# Copy over the custom config *after* compilation and installation
COPY config-docker.json ./dist/share/everest/modules/OCPP/config-docker.json
COPY config.json ./dist/share/everest/modules/OCPP201/config.json
COPY device_model_storage_maeve_sp1.db ./dist/share/everest/modules/OCPP201/device_model_storage.db

COPY run-test.sh /ext/source/tests/run-test.sh

#LABEL org.opencontainers.image.source=https://github.com/everest/everest-demo
