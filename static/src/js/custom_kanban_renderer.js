/** @odoo-module */

import { KanbanRenderer } from "@web/views/kanban/kanban_renderer";

export class CustomKanbanRenderer extends KanbanRenderer {
    setup() {
        super.setup();
        console.log("CustomKanbanRenderer setup");
    }

    customMethod() {
        console.log("Custom method called");
    }

    // Example of a new behavior: log a message when a card is clicked
    onCardClick(event) {
        super.onCardClick(event);
        console.log("Card clicked:", event.currentTarget.dataset.id);
    }
}