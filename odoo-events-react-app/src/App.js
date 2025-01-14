// import React, { useEffect, useState } from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import EventsList from './EventsList'; // Import the EventsList component
// import SignIn from './components/SignIn'; // Import the SignIn component
// import { JWT_TOKEN } from './constants';
//
// function App() {
//   const [jwtToken, setJwtToken] = useState(localStorage.getItem('jwtToken')); // Check if JWT exists in localStorage
//
//   useEffect(() => {
//     // If JWT token is not in localStorage, the user is not authenticated
//     const storedJwtToken = localStorage.getItem('jwtToken');
//     setJwtToken(storedJwtToken); // Update state with JWT token from localStorage
//   }, []);
//
//   const handleSignIn = (token) => {
//     setJwtToken(token); // Update state with the JWT token after successful sign-in
//   };
//
//   const handleSignOut = () => {
//     setJwtToken(null); // Remove JWT token from state
//     localStorage.removeItem('jwtToken'); // Remove JWT from localStorage
//   };
//
//   return (
//     <Router>
//       <div className="App">
//         <Routes>
//           {/* SignIn Route */}
//           <Route path="/" element={<SignIn onSignIn={handleSignIn} />} />
//
//           {/* Events List Route - Only accessible if user is signed in */}
//           <Route
//             path="/events"
//             element={jwtToken ? <EventsList /> : <SignIn onSignIn={handleSignIn} />}
//           />
//         </Routes>
//
//         {/* If user is signed in, show sign out button */}
//         {jwtToken && (
//           <div>
//             <button onClick={handleSignOut}>Sign Out</button>
//           </div>
//         )}
//       </div>
//     </Router>
//   );
// }
//
// export default App;
//
//

// import React, { useEffect, useState } from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import EventsList from './EventsList';
// import SignIn from './components/SignIn';
// import SignOut from './components/SignOut'; // Import the SignOut component
// import { JWT_TOKEN } from './constants';
//
// function App() {
//   const [jwtToken, setJwtToken] = useState(localStorage.getItem('jwtToken'));
//
//   useEffect(() => {
//     const storedJwtToken = localStorage.getItem('jwtToken');
//     setJwtToken(storedJwtToken);
//   }, []);
//
//   const handleSignIn = (token) => {
//     setJwtToken(token);
//   };
//
//   const handleSignOut = () => {
//     setJwtToken(null);
//     localStorage.removeItem('jwtToken');
//   };
//
//   return (
//     <Router>
//       <div className="App">
//         <Routes>
//           {/* SignIn Route */}
//           <Route path="/" element={<SignIn onSignIn={handleSignIn} />} />
//
//           {/* Events List Route */}
//           <Route
//             path="/events"
//             element={
//               jwtToken ? (
//                 <>
//                   <EventsList />
//                   <SignOut onSignOut={handleSignOut} />
//                 </>
//               ) : (
//                 <SignIn onSignIn={handleSignIn} />
//               )
//             }
//           />
//         </Routes>
//       </div>
//     </Router>
//   );
// }
//
// export default App;

import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import EventsList from './EventsList'; // Import the EventsList component
import SignIn from './components/SignIn'; // Import the SignIn component
import { JWT_TOKEN } from './constants';

function App() {
  const [jwtToken, setJwtToken] = useState(localStorage.getItem('jwtToken')); // Check if JWT exists in localStorage

  useEffect(() => {
    const storedJwtToken = localStorage.getItem('jwtToken');
    setJwtToken(storedJwtToken);
  }, []);

  const handleSignIn = (token) => {
    setJwtToken(token);
  };


  return (
    <Router>
      <div className="App">
        <Routes>
          {/* SignIn Route */}
          <Route path="/" element={<SignIn onSignIn={handleSignIn} />} />

          {/* Events List Route - Only accessible if user is signed in */}
          <Route
            path="/events"
            element={jwtToken ? <EventsList /> : <SignIn onSignIn={handleSignIn} />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


