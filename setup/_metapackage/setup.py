import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-l10n-switzerland",
    description="Meta package for oca-l10n-switzerland Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-ebill_postfinance>=16.0dev,<16.1dev',
        'odoo-addon-ebill_postfinance_server_env>=16.0dev,<16.1dev',
        'odoo-addon-ebill_postfinance_stock>=16.0dev,<16.1dev',
        'odoo-addon-l10n_ch_account_tags>=16.0dev,<16.1dev',
        'odoo-addon-l10n_ch_mis_reports>=16.0dev,<16.1dev',
        'odoo-addon-l10n_ch_partner_address_street3>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
