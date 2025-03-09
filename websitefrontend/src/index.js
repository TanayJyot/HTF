import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Home from './Homepage/Home';
import About from './Aboutpage/About';
import Projects from './ProjectPage/Product';
import Contact from './ContactPage/Contact';
import AuthPage from './AuthPage';
import OrdersPage from './OrdersPage';
import ItemDefect from './ItemDefect'; // added import
import App from './App';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      { index: true, element: <Home /> },
      { path: 'login', element: <AuthPage onAuth={() => {}} /> },
      { path: 'orders', element: <OrdersPage onReturn={() => {}} /> },
      { path: 'about', element: <About /> },
      { path: 'projects', element: <Projects /> },
      { path: 'contact', element: <Contact /> },
      { path: 'itemdefect', element: <ItemDefect /> }, // added route
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
);
