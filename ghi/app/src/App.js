import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import RentalCreateForm from './RentalCreateForm';
// import Nav from './Nav';


function App() {
  return (
    <BrowserRouter>
    {/* <Nav /> */}
    <div className="container">
      <Routes>
        <Route path="/rentals/create" element={<RentalCreateForm />} />
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
