import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import { Dialog } from "@headlessui/react";

const Button = ({ children, ...props }) => (
  <button className="px-4 py-2 bg-blue-600 text-white rounded" {...props}>{children}</button>
);

const Card = ({ children, className }) => (
  <div className={`bg-white shadow-md rounded-lg ${className}`}>{children}</div>
);

const Input = (props) => (
  <input className="border p-2 w-full rounded" {...props} />
);

const Modal = ({ open, onOpenChange, children }) => (
  open ? (
    <Dialog open={open} onClose={onOpenChange} className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white p-6 rounded-lg">{children}</div>
    </Dialog>
  ) : null
);

const AuthPage = ({ onAuth }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  
  const handleSubmit = () => onAuth();

  return (
    <div className="flex justify-center items-center h-screen">
      <Card className="p-6 w-96">
        <h2 className="text-xl mb-4">Login</h2>
        <Input placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <Input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="mt-2" />
        <Button className="mt-4 w-full" onClick={handleSubmit}>Login</Button>
      </Card>
    </div>
  );
};

const OrdersPage = ({ onReturn }) => {
  return (
    <div className="p-6">
      <h2 className="text-2xl mb-4">Your Orders</h2>
      <Card className="p-4 flex justify-between items-center">
        <div>
          <p>Women's Hydrenalite™ Down A-Line Vest</p>
          <p className="text-gray-500">$139.99</p>
        </div>
        <Button onClick={onReturn}>Return Item</Button>
      </Card>
    </div>
  );
};

const ReturnReasonModal = ({ isOpen, onClose, onProceed }) => {
  return (
    <Modal open={isOpen} onOpenChange={onClose}>
      <Card className="p-6">
        <h2 className="text-xl mb-4">Why are you returning this item?</h2>
        {["The item doesn’t fit", "The item is different than described", "The item arrived damaged", "I changed my mind", "I don’t like the item"].map((reason) => (
          <Button key={reason} variant="outline" className="w-full mt-2" onClick={onProceed}>{reason}</Button>
        ))}
      </Card>
    </Modal>
  );
};

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

const App = () => {
  const [authenticated, setAuthenticated] = useState(false);
  const [showReasonModal, setShowReasonModal] = useState(false);
  const [showDetailsModal, setShowDetailsModal] = useState(false);

  return (
    <Router>
      <Routes>
        <Route path="/" element={authenticated ? <OrdersPage onReturn={() => setShowReasonModal(true)} /> : <AuthPage onAuth={() => setAuthenticated(true)} />} />
      </Routes>
      <ReturnReasonModal isOpen={showReasonModal} onClose={() => setShowReasonModal(false)} onProceed={() => { setShowReasonModal(false); setShowDetailsModal(true); }} />
      <ReturnDetailsModal isOpen={showDetailsModal} onClose={() => setShowDetailsModal(false)} />
    </Router>
  );
};

export default App;