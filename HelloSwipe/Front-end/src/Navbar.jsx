import logo from "./assets/Hello_Fresh_Lockup.png";

export default function Navbar() {
  return (
    <nav>
      <img src={logo} id="navLogo" />
      <div id="navElements">
        <div className="navButtonBox">
          <p className="navButton">Our Plans</p>
        </div>
        <div className="navButtonBox">
          <p className="navButton">About Us</p>
        </div>
        <div className="navButtonBox">
          <p className="navButton">Our Menus</p>
        </div>
        <div className="navButtonBox">
          <p className="navButton">Gift Cards</p>
        </div>
        <div className="navButtonBox">
          <p className="navButton">Sustainability</p>
        </div>
      </div>
      <div id="userProfile"><p>TestUser</p></div>
    </nav>
  );
}
