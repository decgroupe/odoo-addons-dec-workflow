# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Feb 2021

from odoo import api, fields, models


class RefMarketBom(models.Model):
    _inherit = "ref.market.bom"

    @api.model
    def get_default_products(self):
        res = super().get_default_products()
        product_xmlids = [
            "product_workflow_dec.beq_workforce",
            "product_workflow_dec.beq_research_specific_development",
            "product_workflow_dec.beq_workshop_commissioning_tests"
        ]
        for product_xmlid in product_xmlids:
            product_id = self.env.ref(product_xmlid, raise_if_not_found=False)
            if product_id:
                res += product_id
        return res

    @api.model
    def get_labortime_services(self):
        """ Return a list of services use to compute the labor time """
        res = super().get_labortime_services()
        product_xmlids = [
            "product_workflow_dec.beq_workforce",
        ]
        for product_xmlid in product_xmlids:
            product_id = self.env.ref(product_xmlid, raise_if_not_found=False)
            if product_id:
                res += product_id
        return res
