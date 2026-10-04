# Recipes

## CloudConvert: markdown to PDF from a URL (one job)
`cloud_convert-create-job` with tasks:
- `import-1`: `{"operation":"import/url","url":"<raw GitHub or Cloudinary URL>"}`
- `convert-1`: `{"operation":"convert","input":"import-1","input_format":"md","output_format":"pdf"}`
- `export-1`: `{"operation":"export/url","input":"convert-1"}`
Poll with `cloud_convert-get-task` on the export task. Then download the file and upload it to Drive.

## Cloudinary: upload a local file
1. Call `sign-upload` (or `upload-asset` with a public URL source).
2. POST multipart to `https://api.cloudinary.com/v1_1/<cloud>/image/upload` with the signed params. Use `folder=omni-hub/<slug>`, `tags=omni-hub,<slug>`, and `public_id=<name>`.
3. Keep `secure_url` and record it in `08-CONFIG/projects.json` (`cloudinary_card`) or in the README.

## Supabase: upsert docs
Run `python scripts/omnisync.py bundle && python scripts/omnisync.py sql`. Then pass each `build/kb-upsert-NN.sql` to `execute_sql`. The statements are idempotent: an unchanged sha256 means no write.

## Drive: mirror a folder
`gws drive files list` with `q: "name='Omni Knowledge Hub' and mimeType='application/vnd.google-apps.folder' and trashed=false"`. Create the folder if it is missing, then use `gws drive files create --upload <relative path> --json '{"name":..., "parents":[id]}'`. To update a file, use `gws drive files update --upload` with its fileId. Never create duplicates.
