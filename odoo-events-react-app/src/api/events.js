// src/api/events.js
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8069'; // Adjust base URL and port if needed

/**
 * Fetch paginated events from the Odoo API
 * @param {string} jwt - The JWT token for authentication
 * @param {number} pageNumber - Current page number (default is 1)
 * @param {number} pageSize - Number of events per page (default is 5)
 * @returns {Promise<object>} - API response data
 */
export const fetchEvents = async (jwt, pageNumber = 1, pageSize = 5) => {
    try {
        const response = await axios.post('http://localhost:8069/web/api/fetch_events',
            {
                "params": {
                    jwt: jwt,
                    page_number: pageNumber,
                    page_size: pageSize
                },
            });
        return response.data.result;
    } catch (error) {
        console.error('Error fetching events:', error);
        throw error.response?.data || { error: 'An unknown error occurred' };
    }
};

export const createEvent = async (jwt, name, location, date) => {
    try {
        const response = await axios.post('http://localhost:8069/web/api/create_event', {
            "params": {
                jwt: jwt,
                name: name,
                location: location,
                date: date
            }
        });

        // Check if the response indicates failure due to lack of permission or other errors
        if (response.data.result.success === false) {
            const errorMessage = response.data.result.error;
            console.log('Error creating event:', errorMessage);
            // Throw an error with the access denied message
            throw new Error(errorMessage);
        }

        return response.data.result;
    } catch (error) {
        console.error('Error creating event:', error);

        // If the error is due to permission issue, throw a specific message
        if (error.message.includes("Access denied")) {
            throw new Error('You do not have permission to create events. Please contact your administrator.');
        }

        // Handle other errors
        throw error.response?.data || { error: 'An unknown error occurred' };
    }
}

export const updateEvent = async (jwt, eventId, name, location, date) => {
    try {
        const response = await axios.post('http://localhost:8069/web/api/update_event',
            {
                "params": {
                    jwt: jwt,
                    id: eventId,
                    name: name,
                    location: location,
                    date: date
                }
            });
        return response.data.result;
    } catch (error) {
        console.error('Error updating event:', error);
        throw error.response?.data || { error: 'An unknown error occurred' };
    }


}

export const deleteEvent = async (jwt, eventId) => {
    try {
        console.log('delete Event Called');
        const response = await axios.post('http://localhost:8069/web/api/delete_event', {
            "params": {
                jwt: jwt,
                id: eventId
            }
        });

        // Check for success or failure in the response
        if (response.data.result.success === false) {
            const errorMessage = response.data.result.error;
            console.log('Error deleting event..."', errorMessage);
            // Throw an error with the access denied message
            throw new Error(errorMessage);
        }
        return response.data.result;
    } catch (error) {
        console.error('Error Deleting event:', error);

        // If the error is due to permission issue, throw a specific message
        if (error.message.includes("Access denied")) {
            throw new Error('You do not have permission to delete events. Please contact your administrator.');
        }

        // Handle other errors
        throw error.response?.data || { error: 'An unknown error occurred' };
    }
}

export const fetchEventById = async (jwt, eventId) => {
    try {
        const response = await axios.post('http://localhost:8069/web/api/read_event',
            {
                "params": {
                    jwt: jwt,
                    id: eventId
                }
            });
        return response.data.result;
    } catch (error) {
        console.error('Error fetching event by id:', error);
        throw error.response?.data || { error: 'An unknown error occurred' };
    }
}


export const signIn = async (login, password) => {
  try {
    const response = await axios.post('http://localhost:8069/web/api/signin', {
      "params": {
        db: "odoo-16-ee",  // Replace with your database name
        login: login,
        password: password
      }
    });

    console.log(response);

    // Check if the response was successful
    if (response.data.result.success) {
      // If successful, return the token
      const jwtToken = response.data.result.result.token;
      console.log(jwtToken)
      return { success: true, token: jwtToken };
    } else {
      // If not successful, return the message
      return { success: false, message: response.data.result.message };
    }
  } catch (error) {
    console.error('Error signing in:', error);
    throw error.response?.data || { error: 'An unknown error occurred' };
  }
};