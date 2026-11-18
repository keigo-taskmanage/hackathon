import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders image and message', () => {
  render(<App />);
  expect(screen.getByAltText('hasimoto')).toBeInTheDocument();
  expect(screen.getByText('そんなあ、あなたに')).toBeInTheDocument();
});
