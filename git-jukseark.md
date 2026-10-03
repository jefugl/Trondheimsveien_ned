# Git-jukseark

## Når du er usikker: kjør denne først

```bash
git status
```

Viser hvilken branch du står i, hva som er endret, og om du ligger foran eller bak GitHub. Endrer aldri noe, så den er alltid trygg.

---

## Den faste rutinen

### 1. Start en ny oppgave

```bash
git switch main               # gå til main
git pull                      # hent siste versjon fra GitHub
git switch -c navn-på-oppgave # lag ny branch og gå inn i den
```

### 2. Jobb og lagre underveis

```bash
git status                            # se hva som er endret
git add .                             # velg ut alle endringer
git commit -m "kort beskrivelse"      # lagre lokalt
git push -u origin navn-på-oppgave    # første push av branchen
git push                              # alle senere pusher
```

### 3. Få endringene inn i main

På github.com: **Pull requests → New pull request** (eller den gule boksen **Compare & pull request**)
→ base: `main`, compare: din branch → **Create pull request** → **Merge pull request** → **Confirm merge**.

### 4. Rydd opp

```bash
git switch main
git pull
git branch -d navn-på-oppgave                 # slett lokalt
git push origin --delete navn-på-oppgave      # slett på GitHub
```

Så er du tilbake på steg 1.

---

## Orientering: hvor er jeg?

| Kommando | Hva den viser |
|---|---|
| `git status` | Branch, endringer, foran/bak GitHub |
| `git branch` | Lokale branches (`*` = der du står) |
| `git branch -a` | Også branches på GitHub (`remotes/origin/...`) |
| `git log --oneline --graph --all` | Historikken som et tre (trykk `q` for å gå ut) |
| `git remote -v` | Hvilket GitHub-repo mappen er koblet til |
| `git ls-remote --heads origin` | Hvilke branches som faktisk finnes på GitHub |

I PyCharm: fanen **Git** nederst → **Log** viser historikken visuelt.

---

## Nyttige situasjoner

**Hent nye endringer fra main inn i branchen din**
(f.eks. når main har fått noe nytt etter at du laget branchen)

```bash
git switch navn-på-oppgave
git pull origin main
git push
```

**Gi nytt navn til branchen du står i**

```bash
git branch -m nytt-navn
```

**Klone et repo (første gang)**

```bash
cd ~/PycharmProjects
git clone https://github.com/brukernavn/repo.git
```

**Tom mappe vises ikke i git status**
Git sporer bare filer. Legg en tom fil i mappen:

```bash
touch mappenavn/.gitkeep
```

**Fjerne noe fra repoet, men beholde det på Mac-en** (f.eks. `.idea`)

```bash
echo ".idea/" >> .gitignore
git rm -r --cached .idea
git commit -m "Fjernet .idea fra repo"
```

---

## Vanlige feilmeldinger

| Feilmelding | Betyr | Løsning |
|---|---|---|
| `src refspec main does not match any` | Ingen commits ennå | Gjør en `git commit` først |
| `Password authentication is not supported` | GitHub vil ha token, ikke passord | Bruk token som passord (se under) |
| `remote ref does not exist` | Branchen finnes ikke på GitHub | Sjekk skrivefeil, eller den er allerede slettet |
| `not fully merged` | Branchen har commits som ikke er i main | Merge først, eller `git branch -D` for å kaste dem |
| `remote origin already exists` | Repoet er allerede koblet til GitHub | Sjekk med `git remote -v` |

---

## Token (innlogging fra terminalen)

1. github.com → profilbilde → **Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. **Generate new token (classic)** → huk av **repo** og **workflow** → **Generate token**
3. Kopier tokenen med en gang (vises bare én gang)
4. Ved `git push`: Username = `jefugl`, Password = lim inn tokenen

**Mac-boksen "git-credential-osxkeychain vil bruke ..."** spør etter **Mac-passordet ditt**, ikke tokenen. Trykk **Tillat alltid**.

**Når tokenen utløper:** lag en ny, og slett den gamle fra nøkkelringen:

```bash
printf "protocol=https\nhost=github.com\n\n" | git credential-osxkeychain erase
```

---

## GitHub Actions (pipelines)

- Ligger i fanen **Actions** på GitHub
- Workflow-filer ligger i `.github/workflows/` og slutter på `.yml`
- Når en workflow er merget inn i main, følger den med alle nye branches automatisk
- YAML-felle: `: ` (kolon + mellomrom) inne i tekst skaper feil. Sett hele linjen i enkle anførselstegn:

```yaml
- run: 'echo "Branch: $GITHUB_REF_NAME"'
```

---

## PyCharm-snarveier

| Snarvei | Handling |
|---|---|
| Cmd+T | Pull |
| Cmd+K | Commit |
| Cmd+Shift+K | Push |
| Cmd+Alt+L | Rydd opp formatering |

---

## Gode vaner

- Kjør `git status` ofte, spesielt før du gjør noe
- Alltid `git switch main` + `git pull` før du lager ny branch
- Én branch per oppgave, navngitt etter hva du gjør: `nye-bilder`, `fiks-index`
- Små bokstaver og bindestrek i branch-navn, ingen mellomrom eller æøå
- Commit ofte, med korte og tydelige beskrivelser
- Bruk **Tab** for å fullføre branch- og filnavn og unngå skrivefeil
