import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';
import './CreateListing.css';

function CreateListing() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [location, setLocation] = useState('');
  const [guests, setGuests] = useState('');
  const [beds, setBeds] = useState('');
  const [baths, setBaths] = useState('');
  const [amenities, setAmenities] = useState([]);
  const [showAmenities, setShowAmenities] = useState(false);

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };

  const handlePriceChange = (event) => {
    setPrice(event.target.value);
  };

  const handleLocationChange = (event) => {
    setLocation(event.target.value);
  };

  const handleGuestsChange = (event) => {
    setGuests(event.target.value);
  };

  const handleBedsChange = (event) => {
    setBeds(event.target.value);
  };

  const handleBathsChange = (event) => {
    setBaths(event.target.value);
  };

  const handleAmenitiesChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setAmenities([...amenities, value]);
    } else {
      setAmenities(amenities.filter((amenity) => amenity !== value));
    }
  };

  const handleAmenitiesButtonClick = () => {
    setShowAmenities(true);
  };

  const handleAmenitiesModalClose = () => {
    setShowAmenities(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // code to submit listing data to server
  };

  return (
    <div className="create-listing-container">
      <h1>Create Your Listing</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title:</label>
        <input type="text" id="title" value={title} onChange={handleTitleChange} />

        <label htmlFor="description">Description:</label>
        <textarea id="description" value={description} onChange={handleDescriptionChange} />

        <label htmlFor="price">Price:</label>
        <input type="number" id="price" value={price} onChange={handlePriceChange} />

        <label htmlFor="location">Location:</label>
        <input type="text" id="location" value={location} onChange={handleLocationChange} />

        <label htmlFor="guests">Guests:</label>
        <input type="number" id="guests" value={guests} onChange={handleGuestsChange} />

        <label htmlFor="beds">Beds:</label>
        <input type="number" id="beds" value={beds} onChange={handleBedsChange} />

        <label htmlFor="baths">Baths:</label>
        <input type="number" id="baths" value={baths} onChange={handleBathsChange} />

        <button type="button" onClick={handleAmenitiesButtonClick}>Amenities</button>

        <button type="submit">Create Listing</button>
      </form>

      <Modal show={showAmenities} onHide={handleAmenitiesModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>Close</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <label>
            <input type="checkbox" value="Wifi" onChange={handleAmenitiesChange} checked={amenities.includes('Wifi')} /> Wifi
          </label>
          <label>
            <input type="checkbox" value="Kitchen" onChange={handleAmenitiesChange} checked={amenities.includes('Kitchen')} /> Kitchen
          </label>
          <label>
            <input type="checkbox" value="TV" onChange={handleAmenitiesChange} checked={amenities.includes('TV')} /> TV
          </label>
          <label>
            <input type="checkbox" value="Gym" onChange={handleAmenitiesChange} checked={amenities.includes('Gym')} /> Gym
          </label>
          <label>
            <input type="checkbox" value="Swimming pool" onChange={handleAmenitiesChange} checked={amenities.includes('Swimming pool')} /> Swimming pool
          </label>
          <label>
            <input type="checkbox" value="Parking" onChange={handleAmenitiesChange} checked={amenities.includes('Parking')} /> Parking
          </label>
          <label>
            <input type="checkbox" value="Air conditioning" onChange={handleAmenitiesChange} checked={amenities.includes('Air conditioning')} /> Air conditioning
          </label>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleAmenitiesModalClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}


export default CreateListing;
