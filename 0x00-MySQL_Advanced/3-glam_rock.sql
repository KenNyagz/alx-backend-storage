-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name,
   IFNULL(DATEDIFF(IFNULL(split, 2022), formed), IFNULL(2022 - formed, NULL)) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan;
