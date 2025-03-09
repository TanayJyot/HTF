import React, { useState } from "react";
import { Card, Button, Input } from "./UIComponents";
import { useNavigate } from "react-router-dom";

const ItemDefect = () => {
  const navigate = useNavigate();
  const [defectDescription, setDefectDescription] = useState("");
  const [imageFile, setImageFile] = useState(null);
  const [detectedImage, setDetectedImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!imageFile || !defectDescription) {
      alert("Please select an image and describe the defect.");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("image", imageFile);
    formData.append("description", defectDescription);

    try {
      const res = await fetch("/api/upload-defect", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      // Assume backend returns { detectedImageUrl: "..." }
      setDetectedImage(data.detectedImageUrl);
    } catch (error) {
      console.error(error);
      alert("Error sending defect information");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 flex justify-center items-center h-screen">
      <Card className="p-6 w-96">
        <h2 className="text-xl mb-4">Report a Defect</h2>
        {/* ...existing form instructions... */}
        <p>Please upload an image and describe the defect.</p>
        <div className="my-2">
          <label htmlFor="file-upload" className="btn w-full">
            Choose File
            <input
              id="file-upload"
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => setImageFile(e.target.files[0])}
            />
          </label>
        </div>
        <div className="my-2">
          <textarea
            className="border p-2 w-full rounded"
            placeholder="Describe the defect..."
            value={defectDescription}
            onChange={(e) => setDefectDescription(e.target.value)}
          />
        </div>
        <Button className="mt-4 w-full" onClick={handleSubmit}>
          {loading ? "Sending..." : "Submit & Send Data"}
        </Button>
        {detectedImage && (
          <div className="mt-4">
            <p>Backend returned detected defects:</p>
            <img src={detectedImage} alt="Detected Defect" className="w-full" />
          </div>
        )}
        <Button className="mt-4 w-full" onClick={() => navigate(-1)}>
          Go Back
        </Button>
      </Card>
    </div>
  );
};

export default ItemDefect;
