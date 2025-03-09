import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, Button } from "./UIComponents";
import ReturnReasonModal from "./ReturnReasonModal";
import ReturnDetailsModal from "./ReturnDetailsModal";

const OrdersPage = ({ onReturn }) => {
	const [showReturnReason, setShowReturnReason] = useState(false);
	const [showDetails, setShowDetails] = useState(false);
  const navigate = useNavigate();

	return (
		<div className="p-6">
			<h2 className="text-2xl mb-4">Your Orders</h2>
			<Card className="p-4 flex justify-between items-center">
				<div>
					<p>Women's Hydrenalite™ Down A-Line Vest</p>
					<p className="text-gray-500">$139.99</p>
				</div>
				<Button onClick={() => setShowReturnReason(true)}>Return Item</Button>
			</Card>
			<ReturnReasonModal 
				isOpen={showReturnReason} 
				onClose={() => setShowReturnReason(false)} 
				onProceed={(reason) => {
          setShowReturnReason(false);
          if (reason === "The item arrived damaged") {
            navigate('/itemdefect');
          } else {
            setShowDetails(true);
          }
        }} 
			/>
			<ReturnDetailsModal 
				isOpen={showDetails} 
				onClose={() => setShowDetails(false)} 
			/>
		</div>
	);
};

export default OrdersPage;