
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTachometerAlt, faDollarSign, faCogs, faPlug, faChartBar, faLeaf } from "@fortawesome/free-solid-svg-icons";
import '../styles/Sidebar.css'; // Sidebar styles

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>ENERGY MONiTOR</h2>
      </div>
      <nav className="sidebar-nav">
        <ul>
          <li>
            <NavLink to="/" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faTachometerAlt} className="icon" /> Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink to="/cost" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faDollarSign} className="icon" /> Cost
            </NavLink>
          </li>
          <li>
            <NavLink to="/appliances" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faPlug} className="icon" />  Appliances
            </NavLink>
          </li>
          <li>
            <NavLink to="/usage-by-rooms" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faChartBar} className="icon" /> Usage-by-rooms
            </NavLink>
          </li>
          <li>
            <NavLink to="/emmisions" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faLeaf} className="icon" /> Emmissions
            </NavLink>
          </li>
          <li>
            <NavLink to="/settings" className={({ isActive }) => isActive ? "active link" : "link"}>
                <FontAwesomeIcon icon={faCogs} className="icon" /> Settings
            </NavLink>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
