import React from "react";
import { Modal, Card, Button } from "./UIComponents";

const ReturnReasonModal = ({ isOpen, onClose, onProceed }) => {
	return (
		<Modal open={isOpen} onOpenChange={onClose}>
			<Card className="p-6">
				<h2 className="text-xl mb-4">Why are you returning this item?</h2>
				{[
          "The item doesn’t fit",
          "The item is different than described",
          "The item arrived damaged",
          "I changed my mind",
          "I don’t like the item"
        ].map((reason) => (
					<Button
            key={reason}
            variant="outline"
            className="w-full mt-2"
            onClick={() => onProceed(reason)}>
						{reason}
					</Button>
				))}
			</Card>
		</Modal>
	);
};

export default ReturnReasonModal;