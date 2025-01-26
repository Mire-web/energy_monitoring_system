# Energy Monitoring System - Frontend

![Project Logo](https://via.placeholder.com/150) <!-- Replace with actual logo if available -->

The **Frontend** of the Energy Monitoring System is a React-based web application that provides an intuitive and interactive user interface for monitoring and managing energy consumption. It communicates with the backend API to fetch real-time data, display energy usage statistics, and allow users to interact with the system.

---

## Features

- **Real-Time Data Visualization**: Interactive charts and graphs to display energy consumption in real-time.
- **User Authentication**: Secure login and registration system for users.
- **Device Management**: Add, remove, and manage energy-consuming devices.
- **Dashboard**: Centralized view of energy usage, historical data, and trends.
- **Alerts and Notifications**: Notify users of unusual energy consumption patterns.
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices.

---

## Technologies Used

- **React.js**: JavaScript library for building user interfaces.
- **Redux**: State management library for React.
- **Axios**: HTTP client for making API requests to the backend.
- **Chart.js**: Library for rendering interactive charts and graphs.
- **Material-UI**: React components for a modern and responsive UI design.
- **React Router**: For handling navigation and routing within the app.
- **Socket.IO**: For real-time updates from the backend.

---

## Installation

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)
- Backend server running (for API communication)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mire-web/energy_monitoring_system.git
   cd energy_monitoring_system/frontend/energy_monitor
   
2. **Install Dependencies**
   ```bash
   npm install
   ```
3. **Set Up Environment Variables**
   `REACT_APP_API_URL=http://localhost:5000`
4. **Run the Development Server**
   `npm start`
5. **Access the Application**
   Open your browser and navigate to http://localhost:3000
