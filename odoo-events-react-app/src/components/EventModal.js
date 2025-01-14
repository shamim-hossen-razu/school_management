// import React from 'react';
//
// const EventModal = ({ isOpen, event, onClose, onSave, onChange }) => {
//   if (!isOpen) return null;
//
//   const { name, location, date } = event;
//
//   return (
//     <div className="modal">
//       <h2>{event.id ? 'Update Event' : 'Create New Event'}</h2>
//       <label>
//         Name:
//         <input
//           type="text"
//           value={name}
//           onChange={(e) => onChange({ ...event, name: e.target.value })}
//         />
//       </label>
//       <label>
//         Location:
//         <input
//           type="text"
//           value={location}
//           onChange={(e) => onChange({ ...event, location: e.target.value })}
//         />
//       </label>
//       <label>
//         Date:
//         <input
//           type="date"
//           value={date}
//           onChange={(e) => onChange({ ...event, date: e.target.value })}
//         />
//       </label>
//       <button onClick={onSave}>{event.id ? 'Update' : 'Create'}</button>
//       <button onClick={onClose}>Cancel</button>
//     </div>
//   );
// };
//
// export default EventModal;

import React from 'react';

const EventModal = ({ isOpen, event, onClose, onSave, onChange }) => {
  if (!isOpen) return null;

  const { name, location, date } = event;

  return (
    <div className="modal fade show" style={{ display: 'block' }} tabIndex="-1">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">
              {event.id ? 'Update Event' : 'Create New Event'}
            </h5>
            <button
              type="button"
              className="btn-close"
              onClick={onClose}
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">
            <div className="mb-3">
              <label className="form-label">Name</label>
              <input
                type="text"
                className="form-control"
                value={name}
                onChange={(e) => onChange({ ...event, name: e.target.value })}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Location</label>
              <input
                type="text"
                className="form-control"
                value={location}
                onChange={(e) => onChange({ ...event, location: e.target.value })}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Date</label>
              <input
                type="date"
                className="form-control"
                value={date}
                onChange={(e) => onChange({ ...event, date: e.target.value })}
              />
            </div>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-primary"
              onClick={onSave}
            >
              {event.id ? 'Update' : 'Create'}
            </button>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={onClose}
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EventModal;

