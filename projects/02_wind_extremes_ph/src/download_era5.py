import cdsapi
from pathlib import Path
from src.config import PH_BBOX, YEARS, RAW_DIR

def download_era5_wind_year(out_path: str, year: int, bbox):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    print("Creating CDS client...")
    c = cdsapi.Client()

    print("Requesting ERA5...")
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": ["10m_u_component_of_wind", "10m_v_component_of_wind"],
            "year": str(year),
            "month": [f"{m:02d}" for m in range(1, 13)],
            "day": [f"{d:02d}" for d in range(1, 32)],
            "time": [f"{h:02d}:00" for h in range(0, 24)],
            "area": bbox,
            "format": "netcdf",
        },
        out_path
    )
    print("Done:", out_path)

def main():
    print("YEARS:", YEARS)
    print("BBOX:", PH_BBOX)

    for yr in YEARS:
        out = f"{RAW_DIR}/era5_u10v10_{yr}_PH.nc"
        print(f"Downloading {yr} -> {out}")
        download_era5_wind_year(out, yr, PH_BBOX)

if __name__ == "__main__":
    main()

