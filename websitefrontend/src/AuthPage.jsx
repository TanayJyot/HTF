import React, { useState } from "react";
import { Card, Input, Button } from "./UIComponents";

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

export default AuthPage;