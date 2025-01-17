import { Routes, Route } from "react-router-dom";
import About from './About';
import Dashboard from './Dashboard';
import Home from './Home';
import Layout from './Layout';
export default function App() {
    return (
      <div>
          <nav>
              <div>
                  <Routes>
                      <Route path="/" element={<Layout />}>
                          <Route index element={<Home />} />
                          <Route path="about" element={<About />} />
                          <Route path="dashboard" element={<Dashboard />} />

                          {/* Using path="*"" means "match anything", so this route
                              acts like a catch-all for URLs that we don't have explicit
                              routes for. */}
                          <Route path="*" element={<Home />} />
                      </Route>
                  </Routes>
              </div>
          </nav>
      </div>
    )
}
