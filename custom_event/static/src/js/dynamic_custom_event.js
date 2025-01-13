odoo.define('custom_event.dynamic', function (require) {
    'use strict';
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');

    var DynamicCustomEvent = PublicWidget.Widget.extend({
        selector: '.custom_event',
        start: function () {
            var self = this;
            rpc.query({
                route: '/web/api/events',
                params: {},
            }).then(function (result) {
                console.log(result)
                var events = result.events;
                var $container = self.$el.find('.row');
                $container.empty();
                events.forEach(function (event) {
                    var $eventDiv = $('<div class="col-md-12">');
                    $eventDiv.append('<h2>' + event.name + '</h2>');
                    $eventDiv.append('<p>' + event.location + '</p>');
                    $eventDiv.append('<p>' + event.date + '</p>');
                    $container.append($eventDiv);
                });
            });
        },
    });

    PublicWidget.registry.dynamic_snippet_blog = DynamicCustomEvent;
    return DynamicCustomEvent;
});