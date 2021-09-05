# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2021

from odoo import models, api, fields

SUBTASKS_SUBTYPE = "project_task_subtask.subtasks_subtype"


class ProjectTask(models.Model):
    _inherit = "project.task"

    default_user = fields.Many2one("res.users", compute="_compute_default_user")

    @api.multi
    def send_subtask_email(
        self,
        subtask_name,
        subtask_state,
        subtask_reviewer_id,
        subtask_user_id,
        old_name=None,
    ):
        subtask_user = self.env["res.users"].browse(subtask_user_id)
        if self.env.user != subtask_user:
            super().send_subtask_email(
                subtask_name,
                subtask_state,
                subtask_reviewer_id,
                subtask_user_id,
                old_name=old_name,
            )

    @api.multi
    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        subtype = kwargs.get('subtype', False)
        if subtype and SUBTASKS_SUBTYPE in subtype:
            kwargs.pop('partner_ids', False)
        return super().message_post(**kwargs)

    @api.multi
    def _compute_default_user(self):
        """ Override default compute since nothing is logic in original module
            computation
        """
        for record in self:
            record.default_user = self.env.user
