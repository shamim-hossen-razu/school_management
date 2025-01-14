import React from 'react';

const PaginationControls = ({ pageNumber, onPageChange, hasNext }) => {
  return (
    <div>
      <button
        onClick={() => onPageChange(pageNumber - 1)}
        disabled={pageNumber === 1}
      >
        Previous
      </button>
      <span>Page {pageNumber}</span>
      <button
        onClick={() => onPageChange(pageNumber + 1)}
        disabled={!hasNext}
      >
        Next
      </button>
    </div>
  );
};

export default PaginationControls;
