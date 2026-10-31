FROM alpine:3.20
RUN apk add --no-cache goaccess tzdata
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN mkdir -p /srv/logs /srv/report && chown -R appuser:appgroup /srv/logs /srv/report
USER appuser
WORKDIR /srv
COPY --chown=appuser:appgroup goaccess.conf /etc/goaccess/goaccess.conf
ENTRYPOINT ["sh", "-c", "touch /srv/logs/tp4.log && goaccess --config-file=/etc/goaccess/goaccess.conf"]
