import cdsapi
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-single-levels",
    {
        "product_type": "reanalysis",
        "variable": ["10m_u_component_of_wind", "10m_v_component_of_wind"],
        "year": "2020",
        "month": "01",
        "day": "01",
        "time": "00:00",
        # tiny test box near Manila: [N, W, S, E]
        "area": [15.5, 120.5, 14.0, 121.8],
        "format": "netcdf",
    },
    "data/raw/_test_era5_u10v10.nc",
)

print("Downloaded: data/raw/_test_era5_u10v10.nc")
