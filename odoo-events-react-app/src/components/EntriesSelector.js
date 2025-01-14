// import React from 'react';
//
// const EntriesSelector = ({ pageSize, onPageSizeChange }) => {
//   return (
//     <div>
//       Show
//       <input
//         type="number"
//         value={pageSize}
//         onChange={(e) => onPageSizeChange(Number(e.target.value))}
//         min={1}
//       />
//       entries
//     </div>
//   );
// };
//
// export default EntriesSelector;

import React from 'react';

const EntriesSelector = ({ pageSize, onPageSizeChange }) => {
  return (
    <div className="d-flex align-items-center mb-3">
      <label htmlFor="pageSize" className="me-2">
        Show
      </label>
      <input
        id="pageSize"
        type="number"
        className="form-control me-2"
        style={{ width: '80px' }}
        value={pageSize}
        onChange={(e) => onPageSizeChange(Number(e.target.value))}
        min={1}
      />
      <span>entries</span>
    </div>
  );
};

export default EntriesSelector;

