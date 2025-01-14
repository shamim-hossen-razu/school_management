// import React from 'react';
// import { useNavigate } from 'react-router-dom';
//
// const SignOut = ({ onSignOut }) => {
//   const navigate = useNavigate();
//
//   const handleSignOut = () => {
//     // Clear the JWT token from localStorage
//     localStorage.removeItem('jwtToken');
//
//     // Notify the parent component about the sign-out
//     onSignOut();
//
//     // Redirect to the Sign In page after sign-out
//     navigate('/signin');
//   };
//
//   return (
//     <div>
//       <button onClick={handleSignOut}>Sign Out</button>
//     </div>
//   );
// };
//
// export default SignOut;
import React from 'react';
import { useNavigate } from 'react-router-dom';

const SignOut = ({ onSignOut }) => {
  const navigate = useNavigate();

  const handleSignOut = () => {
    // Clear the JWT token from localStorage
    localStorage.removeItem('jwtToken');

    // Notify the parent component about the sign-out
    onSignOut();

    // Redirect to the Sign In page after sign-out
    navigate('/');
  };

  return (
    <div className="d-flex justify-content-center align-items-center mt-3">
      <button className="btn btn-danger" onClick={handleSignOut}>
        Sign Out
      </button>
    </div>
  );
};

export default SignOut;
