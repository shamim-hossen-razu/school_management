/** @odoo-module */

import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { CustomKanbanRenderer } from "./custom_kanban_renderer";

export const customKanbanView = {
    ...kanbanView,
    Renderer: CustomKanbanRenderer,
};

registry.category("views").add("custom_kanban", customKanbanView);