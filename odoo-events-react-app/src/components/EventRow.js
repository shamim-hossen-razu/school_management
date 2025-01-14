import React from 'react';

const EventRow = ({ event, onUpdate, onDelete }) => {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center">
      <div>
        <strong>{event.id} - {event.name}</strong>
        <p className="mb-1 text-muted">
          {event.location} on {event.date}
        </p>
      </div>
      <div>
        <button
          className="btn btn-danger btn-sm me-2"
          onClick={() => onDelete(event.id)}
        >
          Delete
        </button>
        <button
          className="btn btn-primary btn-sm"
          onClick={() => onUpdate(event)}
        >
          Update
        </button>
      </div>
    </li>
  );
};

export default EventRow;
