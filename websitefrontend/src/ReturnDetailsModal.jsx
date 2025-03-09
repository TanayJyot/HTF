import React from "react";
import { Modal, Card, Button } from "./UIComponents";

const ReturnDetailsModal = ({ isOpen, onClose }) => {
	return (
		<Modal open={isOpen} onOpenChange={onClose}>
			<Card className="p-6">
				<h2 className="text-xl mb-4">Return Details</h2>
				<p><strong>Return Value:</strong> $139.99</p>
				<Button className="mt-4 w-full">Confirm Return</Button>
			</Card>
		</Modal>
	);
};

export default ReturnDetailsModal;