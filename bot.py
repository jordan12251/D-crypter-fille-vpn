#!/usr/bin/env python3
# decrypt_sim.py — simulation de "décryptage" (sécuritaire / éducatif)

import time
import argparse
import sys

def simulate_decrypt(filename, minutes=12, fast=False, pasted_text=None):
    per_minute = 0.5 if fast else 60  # durée d'une "minute" en secondes (fast pour tester)
    print(f"\n🔐 Décryptage de « {filename} » en cours... Patientez environ {minutes} minute(s).\n")
    for i in range(1, minutes + 1):
        # message intermédiaire
        print(f"⏳ {i}/{minutes} minute(s) — Décryptage en cours...")
        # petite animation simple (3 étapes)
        for tick in range(3):
            sys.stdout.write(" .")
            sys.stdout.flush()
            time.sleep(per_minute / 3)
        print()  # nouvelle ligne après animation
    print("\n✅ Décryptage terminé (simulation). Résultat :\n")
    # Afficher un petit "résultat" fictif (ne contient pas de données privées)
    if pasted_text:
        snippet = pasted_text.strip().replace("\n", " ")[:200]
        print(f"(Simulation) Aperçu du contenu collé : « {snippet} »\n")
    else:
        print("(Simulation) Fichier traité — contenu simulé disponible.\n")

def main():
    parser = argparse.ArgumentParser(description="Simulation de décryptage (sécuritaire).")
    parser.add_argument("file", nargs="?", help="Nom du fichier ou étiquette (ex: mina.txt).")
    parser.add_argument("--fast", action="store_true", help="Mode rapide (pour tests).")
    parser.add_argument("--minutes", type=int, default=12, help="Durée en minutes à simuler (défaut 12).")
    parser.add_argument("--paste", action="store_true", help="Permet de coller du texte (stdin).")
    args = parser.parse_args()

    if args.paste:
        print("📋 Colle ton texte maintenant, puis fais Ctrl+D (ou Ctrl+Z puis Entrée sur Windows) :")
        pasted = sys.stdin.read()
    else:
        pasted = None

    if args.file:
        filename = args.file
    else:
        filename = input("📁 Entrez le nom du fichier à 'décrypter' (ex: mina.txt) : ").strip() or "fichier_simulé"

    simulate_decrypt(filename, minutes=args.minutes, fast=args.fast, pasted_text=pasted)

if __name__ == "__main__":
    main()
