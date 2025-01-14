// import React, {useEffect, useState} from 'react';
// import {fetchEvents, createEvent, deleteEvent, updateEvent} from './api/events';
// import EventRow from './components/EventRow';
// import EventModal from './components/EventModal';
// import PaginationControls from './components/PaginationControls';
// import EntriesSelector from './components/EntriesSelector';
// import {useNavigate} from 'react-router-dom';
//
// const EventsList = () => {
//     const [events, setEvents] = useState([]);
//     const [error, setError] = useState(null);
//     const [pageNumber, setPageNumber] = useState(1);
//     const [pageSize, setPageSize] = useState(5);
//     const [showModal, setShowModal] = useState(false);
//     const [eventToEdit, setEventToEdit] = useState({name: '', location: '', date: ''});
//     const navigate = useNavigate(); // To handle navigation (redirect to login if necessary)
//
//     const jwtToken = localStorage.getItem('jwtToken'); // Retrieve JWT from localStorage
//
//     useEffect(() => {
//         if (!jwtToken) {
//             setError('You must be logged in to view events');
//             return;
//         }
//
//         const loadEvents = async () => {
//             try {
//                 const data = await fetchEvents(jwtToken, pageNumber, pageSize);
//                 setEvents(data.events);
//             } catch (err) {
//                 setError(err.error || 'Failed to fetch events');
//             }
//         };
//
//         loadEvents();
//     }, [pageNumber, pageSize, jwtToken]); // Add jwtToken to dependencies to react to changes
//
//     const handleSaveEvent = async () => {
//         if (!jwtToken) {
//             setError('You must be logged in to create or update events');
//             return;
//         }
//
//         try {
//             if (eventToEdit.id) {
//                 await updateEvent(jwtToken, eventToEdit.id, eventToEdit.name, eventToEdit.location, eventToEdit.date);
//             } else {
//                 await createEvent(jwtToken, eventToEdit.name, eventToEdit.location, eventToEdit.date);
//             }
//
//             setShowModal(false);
//             const data = await fetchEvents(jwtToken, pageNumber, pageSize);
//             setEvents(data.events);
//         } catch (err) {
//             setError(err.error || 'Error: Access denied: You are not allowed to create \'Custom Event\' (custom.event) records.');
//         }
//     };
//
//     const handleDeleteEvent = async (eventId) => {
//         if (!jwtToken) {
//             setError('You must be logged in to delete events');
//             return;
//         }
//
//         try {
//             const response = await deleteEvent(jwtToken, eventId);
//
//             // Reload the events after deletion
//             const data = await fetchEvents(jwtToken, pageNumber, pageSize);
//             setEvents(data.events);
//
//         } catch (err) {
//             // Catch the error and show it to the user
//             setError(err.message || 'Failed to delete event'); // Display the specific error message
//         }
//     };
//
//
//     const openModal = (event = {name: '', location: '', date: ''}) => {
//         setEventToEdit(event);
//         setShowModal(true);
//     };
//
//     // Handle logout
//     const handleSignOut = () => {
//         localStorage.removeItem('jwtToken');
//         navigate('/login'); // Redirect to login page
//     };
//
//     return (
//         <div>
//             <h1>Events</h1>
//             <EntriesSelector pageSize={pageSize} onPageSizeChange={setPageSize}/>
//             <button onClick={() => openModal()}>Create Event</button>
//             <button onClick={handleSignOut}>Sign Out</button>
//
//             {error && <p style={{color: 'red'}}>{error}</p>}
//
//             <ul>
//                 {events.map((event) => (
//                     <EventRow
//                         key={event.id}
//                         event={event}
//                         onUpdate={openModal}
//                         onDelete={handleDeleteEvent}
//                     />
//                 ))}
//             </ul>
//
//             <PaginationControls
//                 pageNumber={pageNumber}
//                 onPageChange={setPageNumber}
//                 hasNext={events.length === pageSize}
//             />
//
//             <EventModal
//                 isOpen={showModal}
//                 event={eventToEdit}
//                 onClose={() => setShowModal(false)}
//                 onSave={handleSaveEvent}
//                 onChange={setEventToEdit}
//             />
//         </div>
//     );
// };
//
// export default EventsList;


import React, { useEffect, useState } from 'react';
import { fetchEvents, createEvent, deleteEvent, updateEvent } from './api/events';
import EventRow from './components/EventRow';
import EventModal from './components/EventModal';
import PaginationControls from './components/PaginationControls';
import EntriesSelector from './components/EntriesSelector';
import { useNavigate } from 'react-router-dom';

const EventsList = () => {
    const [events, setEvents] = useState([]);
    const [error, setError] = useState(null);
    const [pageNumber, setPageNumber] = useState(1);
    const [pageSize, setPageSize] = useState(5);
    const [showModal, setShowModal] = useState(false);
    const [eventToEdit, setEventToEdit] = useState({ name: '', location: '', date: '' });
    const navigate = useNavigate();

    const jwtToken = localStorage.getItem('jwtToken');

    useEffect(() => {
        if (!jwtToken) {
            setError('You must be logged in to view events');
            return;
        }

        const loadEvents = async () => {
            try {
                const data = await fetchEvents(jwtToken, pageNumber, pageSize);
                setEvents(data.events);
            } catch (err) {
                setError(err.error || 'Failed to fetch events');
            }
        };

        loadEvents();
    }, [pageNumber, pageSize, jwtToken]);

    const handleSaveEvent = async () => {
        if (!jwtToken) {
            setError('You must be logged in to create or update events');
            return;
        }

        try {
            if (eventToEdit.id) {
                await updateEvent(jwtToken, eventToEdit.id, eventToEdit.name, eventToEdit.location, eventToEdit.date);
            } else {
                await createEvent(jwtToken, eventToEdit.name, eventToEdit.location, eventToEdit.date);
            }

            setShowModal(false);
            const data = await fetchEvents(jwtToken, pageNumber, pageSize);
            setEvents(data.events);
        } catch (err) {
            setError(err.error || 'Error: Access denied: You are not allowed to create "Custom Event" records.');
        }
    };

    const handleDeleteEvent = async (eventId) => {
        if (!jwtToken) {
            setError('You must be logged in to delete events');
            return;
        }

        try {
            await deleteEvent(jwtToken, eventId);
            const data = await fetchEvents(jwtToken, pageNumber, pageSize);
            setEvents(data.events);
        } catch (err) {
            setError(err.message || 'Failed to delete event');
        }
    };

    const openModal = (event = { name: '', location: '', date: '' }) => {
        setEventToEdit(event);
        setShowModal(true);
    };

    const handleSignOut = () => {
        localStorage.removeItem('jwtToken');
        navigate('/login');
    };

    return (
        <div className="container mt-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h1 className="text-primary">Events</h1>
                <div>
                    <button className="btn btn-success me-2" onClick={() => openModal()}>
                        <i className="bi bi-plus-circle"></i> Create Event
                    </button>
                    <button className="btn btn-danger" onClick={handleSignOut}>
                        <i className="bi bi-box-arrow-right"></i> Sign Out
                    </button>
                </div>
            </div>

            <div className="mb-3">
                <EntriesSelector pageSize={pageSize} onPageSizeChange={setPageSize} />
            </div>

            {error && <div className="alert alert-danger">{error}</div>}

            <ul className="list-group">
                {events.map((event) => (
                    <EventRow
                        key={event.id}
                        event={event}
                        onUpdate={openModal}
                        onDelete={handleDeleteEvent}
                        className="list-group-item"
                    />
                ))}
            </ul>

            <div className="mt-4">
                <PaginationControls
                    pageNumber={pageNumber}
                    onPageChange={setPageNumber}
                    hasNext={events.length === pageSize}
                />
            </div>

            <EventModal
                isOpen={showModal}
                event={eventToEdit}
                onClose={() => setShowModal(false)}
                onSave={handleSaveEvent}
                onChange={setEventToEdit}
            />
        </div>
    );
};

export default EventsList;
