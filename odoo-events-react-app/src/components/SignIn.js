import React, { useState } from 'react';
import { signIn } from '../api/events'; // Import the sign-in API function
import { useNavigate } from 'react-router-dom'; // For navigation after successful sign-in

const SignIn = ({ onSignIn }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Used to navigate after successful login

  const handleSignIn = async (e) => {
    e.preventDefault();
    setError(null); // Clear any previous errors

    try {
      // Make the API call to sign in, passing only username and password
      const response = await signIn(username, password);

      if (response && response.token) {
        const jwtToken = response.token; // Extract the JWT from the response

        // Store the JWT in localStorage
        localStorage.setItem('jwtToken', jwtToken);

        // Notify the parent component about the sign-in
        onSignIn(jwtToken);

        // Redirect to the Events List page after successful login
        navigate('/events');
      } else {
        throw new Error('Invalid response from server');
      }
    } catch (err) {
      setError('Failed to sign in. Please check your credentials and try again.');
      console.error(err); // Log the error for debugging
    }
  };

  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card mt-5">
            <div className="card-header text-center">
              <h4>Sign In</h4>
            </div>
            <div className="card-body">
              <form onSubmit={handleSignIn}>
                <div className="mb-3">
                  <label className="form-label" htmlFor="username">Username</label>
                  <input
                    type="text"
                    id="username"
                    className="form-control"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label" htmlFor="password">Password</label>
                  <input
                    type="password"
                    id="password"
                    className="form-control"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                <div className="d-grid gap-2">
                  <button type="submit" className="btn btn-primary">Sign In</button>
                </div>
              </form>
              {error && <div className="alert alert-danger mt-3" role="alert">{error}</div>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
