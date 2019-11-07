### TODO:
#### Backend:
(Python)
- [x] sgp4 1.4 to analyze orbits, positions/velocities
- [x] space-track.org's API to get data, easy to parse based on object-type (DEBRIS)
- [] can also extract metadata (mission, country of origin, year) for annotation purposes
- [] translate GPS of current location to position (XYZ)
- [] filter the original list of debris to get the nearby debris only (use python's `filter()` or `map()`)
- [] (idea) filter for points that fall into the same octant

#### Frontend:
(Javascript, WebGL)
- [] WebGL for rendering (doing 3D->2D projection)
- [] display as a circle oriented on compass directions
- [] dynamic: update every second to illustrate updated positon maybe?
- [] background: space lol
- [] ability to click on each one to generate metadata table
- [] annotation option ; bring up captions for each object containing name (maybe also year)
