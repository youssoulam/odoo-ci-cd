FROM odoo:18

USER root

RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copier la configuration
COPY odoo/odoo.conf /etc/odoo/odoo.conf

# Copier les modules personnalisés dans l’image
COPY custom_addons /mnt/custom_addons

RUN chown -R odoo:odoo /mnt/custom_addons
RUN chown -R odoo:odoo /etc/odoo/odoo.conf

USER odoo