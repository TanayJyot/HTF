import React from "react";
import { Dialog } from "@headlessui/react";

export const Button = ({ children, className, ...props }) => (
	<button className={`btn ${className ? className : ""}`} {...props}>
		{children}
	</button>
);
export const Card = ({ children, className }) => (
	<div className={`bg-white shadow-md rounded-lg ${className}`}>
		{children}
	</div>
);
export const Input = (props) => (
	<input className="border p-2 w-full rounded" {...props} />
);
export const Modal = ({ open, onOpenChange, children }) => (
	open ? (
		<Dialog open={open} onClose={onOpenChange} className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
			<div className="bg-white p-6 rounded-lg">{children}</div>
		</Dialog>
	) : null
);