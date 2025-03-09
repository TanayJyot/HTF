import React, { useState } from "react";
import { Modal, Card, Button, Input } from "./UIComponents";

const EditItemModal = ({ isOpen, onClose, item }) => {
  const [age, setAge] = useState("");
  const [photo, setPhoto] = useState(null);
  const [gender, setGender] = useState("");
  const [preferredFit, setPreferredFit] = useState("");
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState("");
  const [recommendedSize, setRecommendedSize] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!age || !photo || !gender || !preferredFit) {
      alert("Please fill required fields: Age, Photo, Gender, and Preferred Fit");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("age", age);
    formData.append("photo", photo);
    formData.append("gender", gender);
    formData.append("preferredFit", preferredFit);
    if (height) formData.append("height", height);
    if (weight) formData.append("weight", weight);
    if (item && item.id) formData.append("itemId", item.id);

    try {
      const res = await fetch("/api/edit-item", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      // Assume backend returns { recommendedSize: "M" }
      setRecommendedSize(data.recommendedSize);
    } catch (error) {
      console.error(error);
      alert("Error sending item details");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Modal open={isOpen} onOpenChange={onClose}>
      <Card className="p-6">
        <h2 className="text-xl mb-4">Edit Item Details</h2>
        <div className="my-2">
          <Input type="number" placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} />
        </div>
        <div className="my-2">
          <label htmlFor="photo-upload" className="btn w-full">
            {photo ? "Change Photo" : "Upload Photo"}
            <input
              id="photo-upload"
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => setPhoto(e.target.files[0])}
            />
          </label>
        </div>
        <div className="my-2">
          <select className="select select-bordered w-full" value={gender} onChange={(e) => setGender(e.target.value)}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </div>
        <div className="my-2">
          <select className="select select-bordered w-full" value={preferredFit} onChange={(e) => setPreferredFit(e.target.value)}>
            <option value="">Preferred Fit</option>
            <option value="Slim">Slim</option>
            <option value="Regular">Regular</option>
            <option value="Loose">Loose</option>
          </select>
        </div>
        <div className="my-2">
          <Input type="number" placeholder="Height (optional)" value={height} onChange={(e) => setHeight(e.target.value)} />
        </div>
        <div className="my-2">
          <Input type="number" placeholder="Weight (optional)" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <Button className="mt-4 w-full" onClick={handleSubmit}>
          {loading ? "Sending..." : "Submit"}
        </Button>
        {recommendedSize && (
          <div className="mt-4">
            <p>Your recommended size is: <strong>{recommendedSize}</strong></p>
          </div>
        )}
        <Button className="mt-4 w-full" onClick={onClose}>Close</Button>
      </Card>
    </Modal>
  );
};

export default EditItemModal;
