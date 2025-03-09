import React from 'react';
import logo from './Homepage/data/image 1.png';
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <div className="flex justify-between mx-5">
            <div className="bg-base-100">
                <a className="btn btn-ghost">
                    Return Key
                </a>
            </div>

            <div className="bg-base-100 flex justify-center items-center">
                <Link to="/" className="btn btn-ghost text-xl font-light font-josephin">Dashboard</Link>
                <Link to="/orders" className="btn btn-ghost text-xl font-light font-josephin">Orders</Link>
                {/* <div className="dropdown dropdown-bottom"> */}
                    <div tabIndex={0} role="button"
                         className="btn btn-ghost text-xl font-light font-josephin">Analytics
                    {/* </div> */}
                    {/* <ul tabIndex={0}
                        className="menu dropdown-content z-[1] p-2 shadow bg-base-100 rounded-box w-52 mt-4">
                        <li><a>Item 1</a></li>
                        <li><a>Item 2</a></li>
                    </ul> */}
                </div>
                <Link to="/about" className="btn btn-ghost text-xl font-light font-josephin">Optimize</Link>
            </div>

        </div>


    );
};

export default Navbar;
