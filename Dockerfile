# ============================================================
# A Mirror of My Becoming — Portfolio Container
# Author: Evelyn Caro
# Purpose: Serve the static portfolio with one command
# ============================================================

FROM nginx:alpine

# Copy the entire site into the nginx web root
COPY . /usr/share/nginx/html/

# Remove files that shouldn't be served
RUN rm -rf /usr/share/nginx/html/.git \
           /usr/share/nginx/html/.github \
           /usr/share/nginx/html/node_modules \
           /usr/share/nginx/html/venv312 \
           /usr/share/nginx/html/.venv

# Expose port 80
EXPOSE 80

# Nginx runs in the foreground by default
CMD ["nginx", "-g", "daemon off;"]
