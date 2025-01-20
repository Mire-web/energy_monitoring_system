import PropTypes from "prop-types";
import '../styles/Container.css'; // Container styles

const Container = ({ children }) => {
  return <div className="container">{children}</div>;
};

Container.propTypes = {
  children: PropTypes.node.isRequired, // Validate that children is passed
};

export default Container;
