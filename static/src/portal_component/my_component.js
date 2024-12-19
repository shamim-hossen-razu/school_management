/** @odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry"

export class MyComponent extends Component {
    static template = "school_management.MyComponent";
    static props = {};
}

registry.category("public_components").add("school_management.MyComponent", MyComponent);